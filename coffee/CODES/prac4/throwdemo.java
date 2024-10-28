class throwdemo{
public static void demo()
{
try{
throw new NullPointerException("Demo Exception");
}catch(NullPointerException e)
{
System.out.println("Exception caught "+e);
throw e;
}
}
public static void main(String[] args){
try{
demo();
}catch(NullPointerException e1)
{
System.out.println("Exception found "+e1);
System.out.println("Good bye...");
}
}
}
