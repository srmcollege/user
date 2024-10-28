class exceptiondemo
{
public static void main(String[] args)
{
int a=10,b=0,c;
System.out.println("Learning exception Handling....");
try{
c=a/b;
System.out.println("Division is "+c);
}catch(ArithmeticException e1)
{
System.out.println("Exception found is "+e1);
System.out.println("Error ");
e1.printStackTrace();
}
}
}

