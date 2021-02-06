import React, { Component } from "react";
import Form from 'react-bootstrap/Form'

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
            <div>
                <Form>
                    <Form.Group>
                        <Form.Control type="twitter_handle"
                                      placeholder="Enter username"
                                      size="lg"
                                      className="w-25"
                                      ref={this.textInput}
                                      onChange={() => this.props.onChange(this.textInput.current.value)}
                                      style={this.determine_style()}/>

                    </Form.Group>
                </Form>
            </div>
        );
    }
}
