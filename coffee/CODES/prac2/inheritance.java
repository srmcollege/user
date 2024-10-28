class A{
int a,b;

void show()
{
System.out.println("Value of a is "+a+" and value of b is "+b);
}
}
class B extends A
{
int c;

void showc()
{
System.out.println("Value of c is "+c);
}

void add()
{
System.out.println("Addition of a,b,c is "+(a+b+c));
}
}

class inheritance{
public static void main(String[] args){
A x=new A();
x.a=5;
x.b=10;
B y=new B();
y.a=10;
y.b=20;
y.c=30;
System.out.println("Content of subclass B");
y.show();
y.showc();
y.add();
}
}