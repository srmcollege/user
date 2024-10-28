import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;

public class AdminServlet extends HttpServlet {
@Override
public void service(HttpServletRequest request,HttpServletResponse response)
throws IOException,ServletException {
PrintWriter pw=response.getWriter();
response.setContentType("text/html"); 
Cookie[] cookies=request.getCookies();
if(cookies!=null){
pw.println("Cookies found...<br>");
String id=cookies[0].getValue();
String password=cookies[1].getValue();
if(id.equals("admin") && password.equals("admin123")){
pw.println("<b>Welcome to ADMIN page</b><br>");
}
else{
pw.println("You are not admin...<br>Please log in with admin identity");
RequestDispatcher rd=request.getRequestDispatcher("index.html");
rd.include(request,response);
}
}else{
pw.println("Login in the system and try to access the admin page");
RequestDispatcher rd=request.getRequestDispatcher("index.html");
rd.include(request,response);
}
}
}

