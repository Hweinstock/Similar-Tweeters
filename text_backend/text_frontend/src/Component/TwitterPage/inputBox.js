import React, { Component } from "react";
import Form from 'react-bootstrap/Form'
import inputBox_styles from "./Styling/inputBox.module.css";

export default class InputBox extends Component {
    constructor(props) {
        super(props);
        this.textInput = React.createRef();
    }

    determine_style(){
        if(this.props.userExists)
        {
            return {backgroundColor: "#6495ED", color: "black"}
        } else {
            return {backgroundColor: "#87CEFA", color: "black"}
        }
    }

    render() {
        return (
            <div style={{width: '100%'}}>
                <Form>
                    <Form.Group>
                        <Form.Control type="twitter_handle"
                                      placeholder="Enter username"
                                      ref={this.textInput}
                                      onChange={() => this.props.onChange(this.textInput.current.value)}
                                      className={inputBox_styles.default}/>
                    </Form.Group>
                </Form>
            </div>
        );
    }
}
