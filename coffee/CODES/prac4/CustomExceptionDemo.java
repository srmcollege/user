class InvalidAgeException extends Exception
{
InvalidAgeException(String s)
{
super(s);
}
}
class CustomExceptionDemo{
static void validate_age(int age)throws
InvalidAgeException{
if(age<18){
throw new InvalidAgeException("Invalid Age Value");
}else{
System.out.println("Eligible for voting");
}
}
public static void main(String[] args)
{
int age=20;
try{
validate_age(age);
}catch(InvalidAgeException e1)
{
System.out.println("Exception found "+e1);
}
}
}

