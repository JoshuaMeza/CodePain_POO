import java.util.ArrayList;
import java.util.Objects;

class Main {
	public static void main(String[] args) {
		
		ArrayList<Device> devices = new ArrayList<>();

		devices.add(new Device(0, true, "TV"));
		devices.add(new Device(0, true, "AC"));
        devices.add(new Device(0, false, "LAPTOP"));

		Device search = new Device(0, false, "AC");
		int exists = devices.indexOf(search);
		if (exists!=-1) {
			System.out.println("\nEl elemento SI existe en la lista\n");
			System.out.println("El dispositivo tiene las siguientes caracteristicas:\n" + search);
            System.out.println("El dispositivo esta en la posicion " + exists + " del arreglo\n");
		} else {
			System.out.println("\nEl elemento NO existe\n");
		}
	}
}
class Device {
    private int Id;
    private boolean Status;
    private String Name;


    public Device() {
    }

    public Device(int Id, boolean Status, String Name) {
        this.Id = Id;
        this.Status= Status;
        this.Name = Name;
    }
	public String toString(){
        String output;
        output = "ID: " + this.Id +"\n" +
                "Status: " + this.Status + "\n"+
                "Name: " + this.Name + "\n";
        return output;
    }

    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Device devices = (Device) o;
        return Float.compare(devices.Id, Id) == 0 
                && Objects.equals(devices.Name, Name) 
				&& Objects.equals(Status,devices.Status);
    }

    public int hashCode() {
        return Objects.hash(Id, Status, Name);
    }
}