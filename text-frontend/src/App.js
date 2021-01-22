import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { submit_texts, get_headers, make_comparison } from "./api.js"

import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import Message from "./Component/Bot/index";
import TextBox from "./Component/TextBox/index"
import CompareButton from "./Component/CompareButton/index"
import GuessBar from "./Component/GuessBar/index"
import ProgressBar from 'react-bootstrap/ProgressBar'
import axios from "axios";
import StatBox from "./Component/StatBox/index"

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}

const tester_data = [
    createData('Text_1', 159, 6.0, 24, 4.0),
    createData('Text_2', 237, 9.0, 37, 4.3),
];

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            text: {
                box1: "",
                box2: ""
            },
            bar_percent: 75,
            data: undefined
        };

        this.handleChange = this.handleChange.bind(this);

    }


    handleChange(event, name) {
        let newText = event.target.value;
        this.setState(prevState => ({
            text: {
                ...prevState.text,
                [name]: newText
            }
        }));
    }


  render() {
    return (
        <div>
            <h1> Text-Analyzer </h1>

            {/*<GuessBar*/}
            {/*    percent={this.state.bar_percent}*/}
            {/*/>*/}

            {/*<h1>{' '}</h1>*/}
            <TextBox
                name="box1"
                handleChange={this.handleChange}
            />

            <TextBox
                name="box2"
                handleChange={this.handleChange}
            />

            <StatBox
                data={this.state.data}
                get_headers={get_headers}
            />

            <CompareButton
                onClick={() => submit_texts(this.state.text)
                    .then(response => make_comparison(response.data.id)
                        .then(second_response => this.setState({data: second_response.data}))
                        .catch(error => console.log(error))
                    .catch( error => console.log(error)))}
            />
        </div>
  );
  }
}


export default App;
