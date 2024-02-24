package ATV_1.JAVA;

public class Airport {
    protected boolean checkRG(String rg) {
        if (rg.equals("RG")) {
            return true;
        } else {
            return false;
        }
    }

    protected boolean checkTicket(String ticket) {
        if (ticket.equals("Passagem")) {
            return true;
        } else {
            return false;
        }
    }

    protected boolean checkBirthDate(String ticketDate, String rgDate) {
        if (ticketDate.equals(rgDate)) {
            return true;
        } else {
            return false;
        }
    }
}