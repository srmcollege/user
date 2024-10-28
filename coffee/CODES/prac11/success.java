import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class success extends HttpServlet {
@Override
protected void service(HttpServletRequest request,
HttpServletResponse response)
throws ServletException, IOException {
response.setContentType("text/html");
PrintWriter pw=response.getWriter();
pw.println("<b>Welcome...</b><br>");
pw.println("This is Success Page...");
}
}

