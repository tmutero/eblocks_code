
import { Component, EventEmitter, OnInit, Output, ElementRef, ViewChild } from '@angular/core';
import { Contact } from '../models/contact';

@Component({
  selector: 'app-contact-form',
  templateUrl: './contact-form.component.html',
  styleUrls: ['./contact-form.component.css']
})
export class ContactFormComponent implements OnInit {

    contact = {} as Contact;

    submitting = false;
    error = false;
    success = false;

    @Output('addContact')
    addContactEmitter = new EventEmitter();

    @ViewChild("contactName")
    contactNameRef!: ElementRef;

    constructor() { }

    ngOnInit(): void {
        
    }

    

    onAddContact() {
        this.submitting = true
        this.clearStatus()
    
        if (this.invalidName() || this.invalidEmail() || this.invalidContactType()
        || this.invalidAddress() || this.invalidSurname() || this.invalidValue()
        || this.invalidCompany()
        ) {
            this.error = true
            return
        }
        
        this.addContactEmitter.emit(this.contact);
        this.contactNameRef.nativeElement.focus();

        this.contact = {} as Contact;

        this.error = false;
        this.success = true;
        this.submitting = false;   
        
        setTimeout(() => {
            this.clearStatus();
        }, 3000);
    }

    clearStatus() {
        this.success = false;
        this.error = false;
    }    

    invalidName() {
        return !this.contact.name || this.contact.name.length == 0;
    }

    invalidContactType() {
        return !this.contact.contactType || this.contact.contactType.length == 0;
    }

    invalidEmail() {
        return !this.contact.email_address || this.contact.email_address.length == 0;
    }  

    invalidValue() {
        return !this.contact.value || this.contact.value.length == 0;
    }  

    invalidSurname() {
        return !this.contact.surname || this.contact.surname.length == 0;
    } 

    invalidCompany() {
        return !this.contact.company || this.contact.company.length == 0;
    }  

    invalidAddress() {
        return !this.contact.address || this.contact.address.length == 0;
    }  

 
   
    
}