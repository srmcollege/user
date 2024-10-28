import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;

public class HelloServlet extends GenericServlet{
@Override
public void service(ServletRequest req,ServletResponse res)
        throws ServletException,IOException{
PrintWriter pw=res.getWriter();
res.setContentType("text/html");
pw.println("<b>Welcome to Servlet Programming</b><br>");
pw.println("Servlets are used to generate dynamic web pages<br>");
}
}

