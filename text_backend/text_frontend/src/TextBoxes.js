import React, { Component } from 'react';
// import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { submit_texts, get_headers, make_comparison, get_text_objects } from "./api.js"

import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import TextBox from "./Component/TextBox/index"
import CompareButton from "./Component/CompareButton/index"
import GuessBar from "./Component/GuessBar/index"
import StatBox from "./Component/StatBox/index"

class TextBoxes extends Component {
    constructor(props) {
        super(props);
        this.state = {
            text: {
                box1: " ",
                box2: " "
            },
            bar_percent: 0,
            data: { textObjects: undefined,
                    comp: undefined}
        };

        this.handleChange = this.handleChange.bind(this);

    }

    retrieve_stats() {
        return get_text_objects(this.state.text)
            .then(response => this.setState(
                {data: { textObjects: response.data,
                               comp: this.state.data.comp}}))
            .catch(error => console.log(error))
    }

    submit_comparison() {
        return submit_texts(this.state.text)
                    .then(response => make_comparison(response.data.id)
                        .then(second_response => this.handle_second_response(second_response))
                        .catch(error => console.log(error))
                    .catch( error => console.log(error)))
    }

    handle_second_response(sec_response) {

        console.log(sec_response.data);
        let result = sec_response.data.result;
        let confidence_percent = (sec_response.data.percent * 100.0).toFixed(2);
        this.setState({bar_percent: confidence_percent});


    }

    handleChange(event, name) {
        let newText = event.target.value;
        this.setState(prevState => ({
            text: {
                ...prevState.text,
                [name]: newText
            }
        }));
        let p = this.retrieve_stats();

    }


  render() {
    return (
        <div>
            <h1> Text-Analyzer </h1>

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

            <GuessBar
                percent={this.state.bar_percent}
            />

            <h1>{' '}</h1>

            <CompareButton
                onClick={() => this.submit_comparison()}
            />


        </div>
  );
  }
}


export default TextBoxes;
