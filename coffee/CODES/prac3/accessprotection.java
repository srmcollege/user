class access{
int a;
public int b;
private int c;
protected int d;

private void display(){
System.out.println("Value of a is "+a);
System.out.println("Value of b is "+b);
System.out.println("Value of c is "+c);
System.out.println("Value of d is "+d);
}
public void show(){
c=30;
display();
}
}

class accessprotection{
public static void main(String[] args){
access obj=new access();
obj.a=10;
obj.b=20;
//obj.c=30;
//obj.display();
obj.d=40;
obj.show();
}
}