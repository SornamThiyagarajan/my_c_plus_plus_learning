int maximum69Number (int num) {
    char str_num[6]; // As per num range constraint restriction num can hold upto 10^4 which is equivalent of 5+1 (6 char including /0)
    sprintf(str_num, "%d",num); //convert num to string 
    for(int i = 0; i < strlen(str_num); i++)
     { 
        //printf("\ni: %d , ch: %c", i, str_num[i]);
        if(str_num[i] == '6'){
            str_num[i] = '9';
            break;
        }
     }
     num = atoi(str_num);

     /* Just to try with a different approach without using atoi conversion for string to num 
     int res = 0; 
     for (int i=0; str_num[i]!='\0'; i++){
        res = res * 10 + (str_num[i] - '0');
     }
     return res;*/
     return num; 
}
