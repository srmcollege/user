import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class login extends HttpServlet {
public void service(HttpServletRequest request,HttpServletResponse response)
throws ServletException, IOException {

PrintWriter pw=response.getWriter();
response.setContentType("text/html");

String uid = request.getParameter("id");
String upassword = request.getParameter("password");

if(uid.equals("admin") && upassword.equals("admin123")){
RequestDispatcher rd=request.getRequestDispatcher("success");
rd.forward(request,response);
}else{
pw.println("You are not admin...Plz try again!");

RequestDispatcher rd=request.getRequestDispatcher("login.html");
rd.include(request,response);
}
}
}

