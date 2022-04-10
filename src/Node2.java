import java.util.ArrayList;

public class Node2 {
    private int name;
    private int x;
    private int y;
    private int score;
    private int price;

    private Node2 prev;
    private ArrayList<Node2> children;

    public Node2(int name, int x, int y, int score, int price, Node2 prev, ArrayList<Node2> children) {
        this.name = name;
        this.x = x;
        this.y = y;
        this.score = score;
        this.price = price;
        this.prev = prev;
        this.children = children;
    }

    public Node2 getPrev() {
        return this.prev;
    }

    public void setPrev(Node2 prev) {
        this.prev = prev;
    }

    public ArrayList<Node2> getChildren() {
        return this.children;
    }

    public void setChildren(ArrayList<Node2> children) {
        this.children = children;
    }

    public Node2 prev(Node2 prev) {
        setPrev(prev);
        return this;
    }

    public Node2 children(ArrayList<Node2> children) {
        setChildren(children);
        return this;
    }

    
    public Node2() {
        children = new ArrayList<Node2>();
    }

    public Node2(int name, int x, int y, int score, int price) {
        children = new ArrayList<Node2>();
        this.name = name;
        this.x = x;
        this.y = y;
        this.score = score;
        this.price = price;
    }
    public void addChild(Node2 n){
        children.add(n);
    }

    public int getName() {
        return this.name;
    }

    public void setName(int name) {
        this.name = name;
    }

    public int getX() {
        return this.x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return this.y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getScore() {
        return this.score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public int getPrice() {
        return this.price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Node2 name(int name) {
        setName(name);
        return this;
    }

    public Node2 x(int x) {
        setX(x);
        return this;
    }

    public Node2 y(int y) {
        setY(y);
        return this;
    }

    public Node2 score(int score) {
        setScore(score);
        return this;
    }

    public Node2 price(int price) {
        setPrice(price);
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Node2)) {
            return false;
        }
        Node2 node2 = (Node2) o;
        return name == node2.name && x == node2.x && y == node2.y && score == node2.score && price == node2.price;
    }

    @Override
    public String toString() {
        return "{" +
            " name='" + getName() + "'" +
            ", x='" + getX() + "'" +
            ", y='" + getY() + "'" +
            ", score='" + getScore() + "'" +
            ", price='" + getPrice() + "'" +
            "}";
    }


}
