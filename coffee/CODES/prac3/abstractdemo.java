abstract class A
{
abstract void show();
//abstract void callme();

void display()
{
System.out.println("I am inside display() of superclass A");
}
}

class B extends A
{
void show(){
System.out.println("I am inside overriden show() in subclass B");
}
}

class abstractdemo{
public static void main(String[] args){
B b=new B();
b.show();
b.display();
}
}

