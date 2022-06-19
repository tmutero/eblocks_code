
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Contact } from '../models/contact';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
    baseUrl = 'http://127.0.0.1:5000';

    constructor(protected http: HttpClient) { }

    getHeaders() {
        const headers = new HttpHeaders()
        .set('X-Auth', 'authKey'); 
        return headers;         
    }      
}

@Injectable({
    providedIn: 'root'
})
export class ContactsApiService extends ApiService {
   
    getAll() {
        const params = new HttpParams() 
            .set('limit', '10') 
            .set('offset', '0');        
        return this.http.get<Contact[]>(`${this.baseUrl}/get_all_contacts`, {params});           
    }

    get(id: number) {
        return this.http.get<Contact>(`${this.baseUrl}/get_contact/${id}`);           
    }    

    create(contact: Contact) {
        const headers = this.getHeaders();
        return this.http.post<Contact>(`${this.baseUrl}/add_contact`, contact, {headers});
    }

    update(contact: Contact) {
        const headers = this.getHeaders();        
        return this.http.put<Contact>(`${this.baseUrl}/update/${contact.id}`, contact, {headers});
    } 
    
    delete(id: number) {
        const headers = this.getHeaders();      
        return this.http.delete(`${this.baseUrl}/delete/${id}`, {headers});
    }    
}