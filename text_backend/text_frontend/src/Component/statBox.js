import React, { Component } from "react";
import { palette } from '@material-ui/system';
import Box from '@material-ui/core/Box';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

export default class StatBox extends Component {

    constructor(props) {
        super(props);
        this.state = {
            headers: []
        };

    }


    componentDidMount() {
        this.props.get_headers()
            .then(result => this.setState({headers: result.data.Headers}))
            .catch(error => console.log(error));
    }

    generate_rows() {
        let rows;

        if (typeof this.props.data.text_objects == 'undefined') {
            rows = [];
        } else {
            rows = new Array(this.props.data.text_objects.length);
            this.props.data.text_objects.forEach(function (item, index) {
                rows[index] = item;
                rows[index].name = index + 1;
        });
        }
        return rows;
    }

    format_data() {
        if (typeof this.props.data != 'undefined') {

            let rows = this.generate_rows(this.props.data);
            let temp2 = (<TableBody>
                {rows.map(row => (
                    <TableRow key={row.name}>
                        <TableCell component="th" scope="row">
                            {row.name}
                        </TableCell>
                        {this.state.headers.map(header => (
                            <TableCell key={[header]} align="right">
                                {row.[header]}
                            </TableCell>
                            )
                        )}
                    </TableRow>
                ))}
            </TableBody>);
            return temp2;
        } else {

            let default_table = ( <TableBody></TableBody> );
            return default_table
        }
    }

    format_headers() {

        return (
            <TableRow>
                <TableCell key={"blank"}> {' '} </TableCell>
                {this.state.headers.map(header =>
                    <TableCell align="right" key={header}>{header}</TableCell>)}
            </TableRow>
        )


    }

    render() {
        const data = this.format_data();
        return (
            <div style={{width: "100%"}}>
            <TableContainer component={Paper}>
                <Table size="small" aria-label="a dense table">
                    <TableHead>
                        {this.format_headers()}
                    </TableHead>
                    {this.format_data()}
                </Table>
            </TableContainer>
            </div>
        );
  }
}