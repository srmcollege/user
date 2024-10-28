class throwsdemo{
static int a=100,b=0,c;
public static void show()throws ArithmeticException
{
c=a/b;
System.out.println("Division is "+c);
}
public static void main(String[] args){
try{
show();
}catch(ArithmeticException e){
System.out.println("Exception found is "+e);
System.out.println("Good bye...");
}
}
}