class arithmetic{
void add(int a,int b)
{
System.out.println("Addition is "+(a+b));
}

void add(int a,int b,int c)
{
System.out.println("Addition is "+(a+b+c));
}
void add(double a,double b)
{
System.out.println("Addition is "+(a+b));
}
public static void main(String[] args)
{
arithmetic a=new arithmetic();
a.add(10,20);
a.add(10,20,30);
a.add(30.7,30.5);
}
}
