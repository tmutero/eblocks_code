
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-loading',
  templateUrl: './loading.component.html',
  styleUrls: ['./loading.component.css']
})
export class LoadingComponent implements OnInit {
    imgPath = require('../../assets/images/loading.gif');

    constructor() { }

    ngOnInit(): void {
    }

}
