install.packages('geometry');
library(geometry);

zero_ = c(1, 0)
one_ = c(0, 1)

ZERO = array(zero_, dim=c(2, 1))
ZERO

ONE = array(one_, dim=c(2, 1))
ONE

dot(ONE, ZERO)
dot(ZERO, ONE)
dot(ONE, ONE)
dot(ZERO, ZERO)

inner_product <- function(vector1, vector2){
  final_vector =array(numeric(),dim=c(length(vector1)*length(vector2),1));
  index=1;
  for (i in 1:length(vector1)){
    for(j in 1:length(vector2)){
      final_vector[index] = vector1[i]* vector2[j];
      index=index+1;
    }
  }
  return(final_vector);
}

inner_product(ZERO, ZERO);
