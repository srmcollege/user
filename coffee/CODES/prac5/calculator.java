import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class calci extends JFrame implements ActionListener{
JTextField t1,t2,t3;
JButton add,sub,mul,div,clear,exit;

calci(String s)
{
super(s);
FlowLayout f=new FlowLayout();
setLayout(f);
Font f1=new Font("Times New Roman",Font.BOLD,20);

JLabel l1=new JLabel("Enter First Number");
JLabel l2=new JLabel("Enter Second Number");
JLabel l3=new JLabel("Result");

t1=new JTextField(10);
t2=new JTextField(10);
t3=new JTextField(10);

add=new JButton("ADD");
sub=new JButton("SUBTRACT");
mul=new JButton("MULTIPLY");
div=new JButton("DIVISION");
clear=new JButton("CLEAR");
exit=new JButton("EXIT");

l1.setFont(f1);l2.setFont(f1);l3.setFont(f1);
t1.setFont(f1);t2.setFont(f1);t3.setFont(f1);
add.setFont(f1);sub.setFont(f1);
mul.setFont(f1);div.setFont(f1);
clear.setFont(f1);exit.setFont(f1);

add.addActionListener(this);
sub.addActionListener(this);
mul.addActionListener(this);
div.addActionListener(this);
clear.addActionListener(this);
exit.addActionListener(this);


JPanel p=new JPanel();
p.setSize(400,300);
p.setLayout(new GridLayout(6,2));
p.add(l1);p.add(t1);
p.add(l2);p.add(t2);
p.add(l3);p.add(t3);
p.add(add);p.add(sub);
p.add(mul);p.add(div);
p.add(clear);p.add(exit);

add(p);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
}

public void actionPerformed(ActionEvent ae)
{
double x=Integer.parseInt(t1.getText());
double y=Integer.parseInt(t2.getText());

if(ae.getSource()==add)
{
t3.setText(""+(x+y));
}
else if(ae.getSource()==sub)
{
t3.setText(""+(x-y));
}
else if(ae.getSource()==mul)
{
t3.setText(""+(x*y));
}
else if(ae.getSource()==div)
{
t3.setText(""+(x/y));
}
else if(ae.getSource()==clear)
{
t1.setText("");
t2.setText("");
t3.setText("");
}
else if(ae.getSource()==exit)
{
System.exit(0);
}
}
}

class calculator{
public static void main(String args[])
{
calci c=new calci("CALCULATOR");
c.setSize(600,400);
c.setVisible(true);
}
}