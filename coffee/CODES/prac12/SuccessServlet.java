import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class SuccessServlet extends HttpServlet{

    @Override
    public void service(HttpServletRequest request,HttpServletResponse response)
            throws ServletException,IOException{
        
        response.setContentType("text/html");
        PrintWriter pw=response.getWriter();
        
        String uid=request.getParameter("id");
        String upassword=request.getParameter("password");
        
        pw.println("Welcome "+uid+" Your password is "+upassword);
        }
    }