awk 'BEGIN{max=0;maxc=0;count=1}{if(NF>0){a+=$1}else{if(a>max){max=a;maxc=count}count=count+1;a=0}}END{print maxc,max}' $1
