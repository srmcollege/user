import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;

public class ArithmeticServlet extends GenericServlet{
@Override
public void service(ServletRequest req,ServletResponse res)
        throws ServletException,IOException{
PrintWriter pw=res.getWriter();
res.setContentType("text/html");
try{
int num1 = Integer.parseInt(req.getParameter("n1"));
int num2 = Integer.parseInt(req.getParameter("n2"));
pw.println("Addition is: "+(num1+num2)+"<br>");
pw.println("Subtraction is: "+(num1-num2)+"<br>");
pw.println("Multiplication is: "+(num1*num2)+"<br>");
pw.println("Division is: "+(num1/num2)+"<br>");
}catch(NumberFormatException e){
pw.println("Please enter valid numbers."+e);
}
}
}

