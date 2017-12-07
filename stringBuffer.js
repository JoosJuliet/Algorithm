var numArray = ['','일','이','삼','사','오','육','칠','팔','구'];
 
 var input = (num) =>{
   num += '';
   if( num === '0'){
     console.log("영");
     return;
   }
   if( num === '1' ){
     console.log('일');
     return;
   }
 
   if ( num.length >5 ) {
     console.log("범위가 초과되었습니다.");
     return;
   }
 
   var answr='';
   var decimal = ['','십','백','천','만'];
   for (var i = 0; i < num.length; i++) {
     if( num[i] === '1' ){
 
         if( i === num.length-1){
           answr += "일";
         }else{
           answr += decimal[num.length-1-i] ; //백
           console.log("if",answr);
         }
      }
 
     else{
       answr += numArray[num[i]] + decimal[ num.length -(i+1)] ;
       //       십               일
       console.log('numArray[num[i]]',numArray[num[i]]);
       console.log('decimal[ num.length -(i+1)]',decimal[ num.length -(i+1)]);
       console.log("else",answr);
       // 십일십
     }
   }
   console.log(answr);
 };
 
 input(11);
