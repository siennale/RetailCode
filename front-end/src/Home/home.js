import React, { useState, useEffect, Component } from 'react';
import './home.css';

import Navbar from 'react-bootstrap/Navbar'
import BarcodeReader from 'react-barcode-reader'


class Home extends Component {

    constructor(props) {
        super(props)
        this.state = {
            result: 'No result',
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
                <Navbar bg="dark">
                    <Navbar.Brand href="#home">
                    </Navbar.Brand>
                </Navbar>


                <div id="page">

                    <div id="sideBar">
                        add billing items here
                    </div>
                    <div id="content">
                        price of the barcode scanned
                    </div>
                    <div>
                        <BarcodeReader
                            onError={this.handleError}
                            onScan={this.handleScan}
                        />
                        <p>{this.state.result}</p>
                    </div>
                </div>


            </div>
        );
    }
}

export default Home;
