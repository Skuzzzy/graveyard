// Credit goes to https://github.com/REALDrummer, I just wrote this during his presentation

import java.io.*;

public class BFToJava {
    public static final String NEW_LINE = System.lineSeparator();
    public static final String HEADER1 = "import java.io.*;" + NEW_LINE +
            "import java.util.Arrays;" + NEW_LINE +
            "public class ";
    public static final String HEADER2 = " {" + NEW_LINE +
            "\tstatic byte[] tape = new byte[200];" + NEW_LINE +
            "\tstatic int tape_index = 0;" + NEW_LINE + NEW_LINE +
            "\tpublic static void main(String[] args) {" + NEW_LINE +
            "\t\tReader in = new InputStreamReader(System.in);" + NEW_LINE +
            "\t\tArrays.fill(tape, (byte)-128);" + NEW_LINE + NEW_LINE +
            "\t\ttry {" + NEW_LINE;
    public static final String FOOTER =
            "\t\t\tin.close();" + NEW_LINE +
            "\t\t} catch (IOException ex) {" + NEW_LINE +
            "\t\t\tex.printStackTrace();" + NEW_LINE +
            "\t\t}" + NEW_LINE +
            "\t}" + NEW_LINE +
            "}";

    public static void printIndentation(BufferedWriter out, int indentation) throws IOException {
        for (int i = 0; i<indentation; i++)
        {
            out.write("\t");
        }
    }

    public static void main(String[] args) {
        File output_file = new File(args[0] + ".java");
        if(output_file.exists()) {
            output_file.delete();
        }

        int indent = 3;

        try {
            output_file.createNewFile();
            BufferedReader in = new BufferedReader(new FileReader(new File(args[0] + ".bf")));
            BufferedWriter out = new BufferedWriter(new FileWriter(output_file));

            out.write(HEADER1 + args[0] + HEADER2);

            int character;
            while((character = in.read()) != -1) {
                switch (character) {
                    case '+':
                        printIndentation(out, indent);
                        out.write("tape[tape_index]++;" + NEW_LINE);
                        break;
                    case '-':
                        printIndentation(out, indent);
                        out.write("tape[tape_index]--;" + NEW_LINE);
                        break;
                    case '<':
                        printIndentation(out, indent);
                        out.write("tape_index--;" + NEW_LINE);
                        break;
                    case '>':
                        printIndentation(out, indent);
                        out.write("tape_index++;" + NEW_LINE);
                        break;
                    case '[':
                        printIndentation(out, indent++);
                        out.write("while(tape[tape_index] != -128) {" + NEW_LINE);
                        break;
                    case ']':
                        printIndentation(out, --indent);
                        out.write("}" + NEW_LINE);
                        break;
                    case '.':
                        printIndentation(out, indent);
                        out.write("System.out.print((char)(tape[tape_index] + 128));" + NEW_LINE);
                        break;
                    case ',':
                        printIndentation(out, indent);
                        out.write("tape[tape_index] = (byte) (in.read() - 128);" + NEW_LINE);
                        break;
                    default:
                        // Ignore other chars
                        break;
                }
            }

            out.write(FOOTER);
            in.close();
            out.close();
        } catch (IOException io) {
            io.printStackTrace();
        }

    }

}
