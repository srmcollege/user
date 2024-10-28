class mycatch{
public static void main(String[] args){
int a=100,b,c;
b=args.length;
int arr[]=new int[10];
try{
c=a/b;
System.out.println("Division is "+c);
arr[12]=200;
}
catch(ArithmeticException e1)
{
System.out.println("Arithmetic Exception found "+e1);
}
catch(ArrayIndexOutOfBoundsException e2)
{
System.out.println("Array Index Exception found "+e2);
}
catch(Exception e3)
{
System.out.println("Exception found "+e3);
}
System.out.println("Good bye...");
}
}

