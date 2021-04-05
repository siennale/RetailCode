import React, {Component } from 'react';
import './home.css';
import axios from 'axios';

import Navbar from 'react-bootstrap/Navbar'
import BarcodeReader from 'react-barcode-reader'

class Home extends Component {

    
    constructor(props) {
        super(props)
        this.state = {
            barcode: 'Please Scan Barcode for Price',
            price: 10,
            currentList : ["Apple", "Pop coke"]
        }

        this.handleScan = this.handleScan.bind(this)
        this.handleDoneBtn = this.handleDoneBtn.bind(this);
        this.handleResetBtn = this.handleResetBtn.bind(this);
        this.addToCurrentList = this.addToCurrentList.bind(this);
    }

    handleScan(data) {
        this.setState({
            result: data,
        })


    }
    handleError(err) {
        console.error(err)
    }

    handleDoneBtn(){
        console.log("donebutton pressed")
        this.setState({
            currentList : []
        }) 
    }

    handleResetBtn(){
        console.log("Rest btn pressed")
        this.setState({
            currentList : [],
        }) 
    }
    
    addToCurrentList(){
        console.log("Adding to current list");
        this.setState({
            currentList : [...this.state.currentList, "s"],
        }) 
    }

    render() {
        return (
            <div className="Home">
                <Navbar class="navbar" bg="dark">
                    <Navbar.Brand href="#home">
                        <div class="navbar-font">Welcome to the portal</div>
                    </Navbar.Brand>
                </Navbar>

                <div id="page">

                    <div id="sideBar">
                        <ul>
                            {this.state.currentList.map(val => {
                                return <li key={val}> {val}</li>
                            })}
                        </ul>

                        <div class="bottom-left">
                            <button type="button" class="btn btn-primary btn-lg doneButton" onClick={this.handleDoneBtn}>Done</button>
                            <button type="button" class="btn btn-primary btn-lg resetButton" onClick={this.handleResetBtn}>Reset</button>
                        </div>
                    </div>

                    <div id="content">
                        <div class="inner-content">
                            <p class="welcome-message">Price of the Product</p>
                            <div class="inner-box">
                                <div class="price-box">
                                    <BarcodeReader
                                        onError={this.handleError}
                                        onScan={this.handleScan}
                                    />
                                    <div>{this.state.barcode}</div>
                                    <br></br>
                                    <div class="original-price">${this.state.price}</div>
                                    <br></br>
                                    <div> GST${(this.state.price * 0.05 + this.state.price).toFixed(2)}, GST+PST ${(this.state.price * 0.12 + this.state.price).toFixed(2)} </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
export default Home;