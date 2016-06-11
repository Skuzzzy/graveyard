#include <iostream>

using namespace std;

char * int_to_hexstring(int32_t n)
{
    const bool negative_p = n < 0;
    int32_t positive_n = (negative_p ? -n : (n));

    char * result;
    int result_fill_index = 0;
    bool allocated = false;


    for(int blockindex=0; blockindex<8; blockindex++)
    {
	int offset = sizeof(int32_t)*8 - 4*blockindex - 4;
	int slice = (positive_n >> offset) & 0xF;
	if((slice != 0 || offset==0) && !allocated){
	    allocated = true;

	    int string_size = (negative_p ? 1 : 0) + 2 + sizeof(int32_t) - blockindex + 1;
	    result = new char[string_size]();
	    if(negative_p)
	    {
		result[result_fill_index] = '-';
		result_fill_index++;
	    }

	    result[result_fill_index] = '0';
	    result_fill_index++;
	    result[result_fill_index] = 'x';
	    result_fill_index++;
	}
	if(allocated)
	{
	    const char char_table[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
	    result[result_fill_index++] = char_table[slice];
	}
    }

    result[result_fill_index] = '\0';
    return result;
}

int main()
{
    int32_t asd = 50;
    char * res = int_to_hexstring(asd);
    cout << res << endl;
    free(res);
    return 0;
}
