#include "foo.h"
using std::cout;
using std::endl;
using std::ifstream;

int main(int argc, char** argv){

  std::ifstream in(argv[1]);
 
  float tot=30;
  if(argc<2){
    return 1;
  }
  if(in.good()){
    //in >> ordNum >> ordLine >> cusNum >> prodNum >> ordPlat >> ordDate >> ordTime >> lineAmt;
    tot += 1;
    printf("This file has content! Hooray! \n");
  }
  in.close();;
  return 0;
}


