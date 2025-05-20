// Name: Carter Landry
// Date: 5/19/25
// Description: This is the SaleItem class made for Program 4.
class SaleItemTest {
// do not edit the contents of this class
// run `java SaleItemTest` to test the code in the SaleItem class
public static void main(String[] args){
        System.out.println("Item\tCost\tPrice\tProfit");
        System.out.println("-".repeat(31));
        SaleItem shoes = new SaleItem();
        SaleItem jeans = new SaleItem();
        SaleItem shirt = new SaleItem();
        System.out.println(shoes);
        System.out.println(jeans);
        System.out.println(shirt);
        System.out.println("-".repeat(31));
        shoes = new SaleItem("Shoes", 30.00, 79.99);
        jeans = new SaleItem("Jeans", 30.00, 50.00);
        shirt = new SaleItem("Shirt", 20.00, 40.00);
        System.out.println(shoes);
        System.out.println(jeans);
        System.out.println(shirt);
        System.out.println("-".repeat(31));
        shoes.setCost(-10);
        jeans.setPrice(2);
        shirt.applySale(50);
        System.out.println(shoes);
        System.out.println(jeans);
        System.out.println(shirt);
    }
}
// create your SaleItem class here
class SaleItem {
    
    // Variables
    private String name;
    private double cost;
    private double price;

    // Constructor
    public SaleItem(String name, double cost, double price) {
        this.name = name;
        this.cost = cost;
        this.price = price;
    }

    // Default Constructor
    public SaleItem() {
        this.name = "Unnamed";
        this.cost = 0;
        this.price = 0;
    }

    // Accessors & Mutators
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getCost() {
        return cost;
    }

    public void setCost(double cost) {
        if (cost < 0) {
            this.cost = 0;
        } else {
            this.cost = cost;
        }
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if (price < 0) {
            this.price = 0;
        } else {
            this.price = price;
        }
    }

    // profit() method: returns the profit of a SaleItem
    public double profit() {
        return (this.price - this.cost);
    }

    // applySale() method: sets the price of a SaleItem given a sale as a percentage
    public void applySale(int sale) {
        this.price = (this.price - (this.price * (sale / 100.0)));
    }

    // toString() method: returns a SaleItem formatte as a String
    @Override
    public String toString() {
        return String.format("%-10s\t%.2f\t%.2f\t%.2f", name, cost, price, profit());
    }
}
