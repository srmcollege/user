class A
{
int a,b;
A(int x,int y)
{
a=x;
b=y;
}
void show()
{
System.out.println("Value of a is "+a+" and value of b is "+b);
}
}
class B extends A
{
int c;
B(int x,int y,int z)
{
super(x,y);
c=z;
}
void showc()
{
System.out.println("Value of c is "+c);
}
}

class superdemo{
public static void main(String[] args)
{
B b=new B(10,20,30);
b.show();
b.showc();
}
}
