import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class hideshow extends JFrame implements ActionListener
{
JTextField t;
JButton b1,b2;

hideshow()
{
setLayout(new FlowLayout());
Font f=new Font("Times New Roman",Font.BOLD,20);

t=new JTextField(20);
b1=new JButton("HIDE");
b2=new JButton("SHOW");
b1.addActionListener(this);
b2.addActionListener(this);

b1.setFont(f);
b2.setFont(f);
add(t);add(b1);add(b2);

setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
}

public void actionPerformed(ActionEvent ae)
{
if(ae.getSource()==b1)
{
t.setVisible(false);
}
else if(ae.getSource()==b2){
t.setVisible(true);
}

}
}

class eventdemo{
public static void main(String args[])
{
hideshow s=new hideshow();
s.setSize(600,400);
s.setVisible(true);
}
}
