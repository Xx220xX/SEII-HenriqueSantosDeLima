#include<stdio.h>
#include<stdlib.h>

int main(int narg, char ** args){
  unsigned buffSize =1024*10000; // 10Mb 
  unsigned bytesReaded;
  char *buff;
  FILE *fin,*fout;
  if(nargs!= 3){
    fprintf(stderr,"Número  de argumentos inválidos\n");
    return -1;
  }
  if (!(fin = fopen(args[1],"rb")){
    fprintf(stderr,"O arquivo %s não  foi encontrado\n",args[1]);
    return -1;
  }if (!(fout = fopen(args[2],"wb")){
    fprintf(stderr,"O arquivo %s não   pode ser criado\n",args[2]);
    return -1;
  }
  buff =(char*) malloc(buffSize);
  if(!buff){
     fprintf(stderr,"Não foi possivel alocar memoria\n");
     goto freeFiles;
  }
  while(!feof(fin)){
    bytesReaded = fread(buff,buffSize,1,fin);
    if(bytesReaded <=0)break;
    fwrite(buff,bytesReaded,1,fout);
  }
  free(buff);
  freeFiles:
  fclose(fin);
  fclose(fout);
  
  return 0;
}


  
