import * as React from "react";
import Button from "@mui/material/Button";
import ButtonGroup from "@mui/material/ButtonGroup";
import { BrowserSerial } from "browser-serial";

export function ButtonSearch() {
  const serial = new BrowserSerial();

  return (
    <ButtonGroup variant="outlined" aria-label="outlined button group">
      <Button
        onClick={() => {
          serial.connect().then(() => console.log(serial));
        }}
      >
        Open Serial Port
      </Button>
      <Button
        onClick={() => {
          serial.disconnect();
        }}
      >
        Close Serial Port
      </Button>
    </ButtonGroup>
  );
}
