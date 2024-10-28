class cover{
cover(int a,int b)
{
System.out.println("Addition is "+(a+b));
}

cover(int c,int d,int e)
{
System.out.println("Substraction is "+(c-d-e));
}

cover(double a,double b)
{
System.out.println("Division is "+(a/b));
}
public static void main(String[] args){
cover x=new cover(10,20);
cover y=new cover(25,7,2);
cover z=new cover(50,25);
}
}