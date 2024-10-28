class A
{
void show()
{
System.out.println("I am inside show() of superclass A");
}
}

class B extends A
{
void show()
{
System.out.println("I am inside show() of subclass B");
super.show();
}
}

class overriding
{
public static void main(String[] args)
{
B b=new B();
b.show();
}
}

