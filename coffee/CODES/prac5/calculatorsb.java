import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class calci2 extends JFrame implements ActionListener {
JTextField t1, t2, t3;
JButton add, sub, mul, div, clear, exit;

calci2(String s) {
super(s);
setLayout(null);
Font f1 = new Font("Times New Roman", Font.BOLD, 20);

JLabel l1 = new JLabel("Enter First Number");
JLabel l2 = new JLabel("Enter Second Number");
JLabel l3 = new JLabel("Result");

t1 = new JTextField(10);
t2 = new JTextField(10);
t3 = new JTextField(10);

add = new JButton("ADD");
sub = new JButton("SUBTRACT");
mul = new JButton("MULTIPLY");
div = new JButton("DIVISION");
clear = new JButton("CLEAR");
exit = new JButton("EXIT");

l1.setFont(f1);
l2.setFont(f1);
l3.setFont(f1);
t1.setFont(f1);
t2.setFont(f1);
t3.setFont(f1);
add.setFont(f1);
sub.setFont(f1);
mul.setFont(f1);
div.setFont(f1);
clear.setFont(f1);
exit.setFont(f1);

l1.setBounds(50, 50, 200, 30);
t1.setBounds(300, 50, 200, 30);
l2.setBounds(50, 100, 200, 30);
t2.setBounds(300, 100, 200, 30);
l3.setBounds(50, 150, 200, 30);
t3.setBounds(300, 150, 200, 30);

add.setBounds(50, 200, 200, 30);
sub.setBounds(300, 200, 200, 30);
mul.setBounds(50, 250, 200, 30);
div.setBounds(300, 250, 200, 30);
clear.setBounds(50, 300, 200, 30);
exit.setBounds(300, 300, 200, 30);

add.addActionListener(this);
sub.addActionListener(this);
mul.addActionListener(this);
div.addActionListener(this);
clear.addActionListener(this);
exit.addActionListener(this);

add(l1);add(t1);
add(l2);add(t2);
add(l3);add(t3);
add(add);add(sub);
add(mul);add(div);
add(clear);add(exit);

setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
}

public void actionPerformed(ActionEvent ae){
double x = Integer.parseInt(t1.getText());
double y = Integer.parseInt(t2.getText());

if(ae.getSource()==add){
t3.setText(""+(x+y));
} else if(ae.getSource()==sub){
t3.setText(""+(x-y));
} else if(ae.getSource()==mul){
t3.setText(""+(x*y));
} else if(ae.getSource()==div){
t3.setText(""+(x/y));
} else if(ae.getSource()==clear){
t1.setText("");
t2.setText("");
t3.setText("");
} else if(ae.getSource()==exit){
System.exit(0);
}
}
}

class calculatorsb{
public static void main(String args[]) {
calci2 c = new calci2("CALCULATOR");
c.setSize(600, 400);
c.setVisible(true);
}
}