import React, { Component } from 'react';
// import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import { submit_texts, make_comparison, get_text_objects } from "./api.js";
import { get_headers } from '../sharedAPIs.js'

import TextBox from "./textBox.js"
import CompareButton from "./compareButton.js"
import GuessBar from "./guessBar.js"
import StatBox from "../statBox.js"

class TextBoxPage extends Component {
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
                {data: {rows: response.data.reports}}))
            .catch(error => console.log(error))
    }

    submit_comparison() {
        return submit_texts(this.state.text)
                    .then(response => this.handle_response(response))
                    .catch( error => console.log(error));
    }

    handle_response(sec_response) {

        let result = sec_response.data.result;
        let confidence_percent = (result.percentage * 100.0).toFixed(2);
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
                title={"Text Statistics"}
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


export default TextBoxPage;
