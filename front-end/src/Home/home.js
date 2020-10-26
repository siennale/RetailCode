import React, { useState, useEffect, Component } from 'react';
import './home.css';

import Navbar from 'react-bootstrap/Navbar'
import BarcodeReader from 'react-barcode-reader'

class Home extends Component {

    constructor(props) {
        super(props)
        this.state = {
            barcode: 'Please Scan Barcode for Price',
            price: 10
        }

        this.handleScan = this.handleScan.bind(this)
    }

    handleScan(data) {
        this.setState({
            result: data,
        })
    }
    handleError(err) {
        console.error(err)
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
                        Billing Items
                    </div>

                    <div id="content">
                        <div class="inner-content">
                            <p class="welcome-message">Price of the Product</p>
                            <div class="inner-box">
                                <p class="price-box">
                                    <BarcodeReader
                                        onError={this.handleError}
                                        onScan={this.handleScan}
                                    />
                                    <div>{this.state.barcode}</div>
                                    <br></br>
                                    <div class="original-price">${this.state.price}</div>
                                    <br></br>
                                    <div> GST${(this.state.price * 0.05 + this.state.price).toFixed(2)}, GST+PST ${(this.state.price * 0.12 + this.state.price).toFixed(2)} </div>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
export default Home;