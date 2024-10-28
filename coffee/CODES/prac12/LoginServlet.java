import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;

public class LoginServlet extends HttpServlet {
@Override
public void doPost(HttpServletRequest request,HttpServletResponse response)
throws IOException, ServletException {
response.setContentType("text/html");
PrintWriter pw = response.getWriter();

String uid=request.getParameter("id");
String upassword=request.getParameter("password");

Cookie c1=new Cookie("id",uid);
Cookie c2=new Cookie("password",upassword);
response.addCookie(c1);
response.addCookie(c2);
pw.println("Cookies are created and stored..."); 

}
}

