import { useState } from "react";
import { ChakraProvider, Box } from "@chakra-ui/react";
import Navbar from "./Navbar/index";
import MainSideBar from "./MainSideBar";
import SummaryBar from "./SummaryBar";
import { Divider, Grid, HStack, VStack } from "@chakra-ui/react";
import BarcodeReader from "react-barcode-reader";
import axios from "axios";

const calculateGST = (scanValue) => {
  if (scanValue && scanValue.data && scanValue.data[4]) {
    return (scanValue.data[3] * 0.05).toFixed(2);
  } else {
    return "0";
  }
};

const calculatePST = (scanValue) => {
  if (scanValue && scanValue.data && scanValue.data[4]) {
    return (scanValue.data[3] * 0.07).toFixed(2);
  } else {
    return "0";
  }
};

const calculateName = (scanValue) => {
  if (scanValue && scanValue.data && scanValue.data[2]) {
    return scanValue.data[2];
  } else {
    return "Scan The Item OR Item not found ";
  }
};

const calculatePrice = (scanValue) => {
  if (scanValue && scanValue.data && scanValue.data[3]) {
    return scanValue.data[3];
  } else {
    return "0";
  }
};

const calculateTotal = (scanValue) => {
  if (scanValue && scanValue.data && scanValue.data[4]) {
    return (scanValue.data[3] * 1.12).toFixed(2);
  } else {
    return "0";
  }
};

export default function App() {
  const [scanData, setScanData] = useState([]);
  const [gst, setGST] = useState(calculateGST(0));
  const [pst, setPST] = useState(calculatePST(0));
  const [itemName, setItemName] = useState(calculateName(0));
  const [price, setPrice] = useState(calculatePrice(0));
  const [total, setTotal] = useState(calculateTotal(0));

  const resetData = () => {
    setScanData([]);
    setGST(calculateGST(0));
    setPST(calculatePST(0));
    setItemName(calculateName(0));
    setPrice(calculatePrice(0));
    setTotal(calculateTotal(0));
  };

  const handleScan = (data) => {
    axios
      .get("http://localhost:5001/product?barcode=" + data)
      .then((res: any) => {
        if (res.data != null) setScanData(scanData.concat(res));
        if (scanData.length > 15) setScanData([]);
        setGST(calculateGST(res));
        setPST(calculatePST(res));
        setItemName(calculateName(res));
        setPrice(calculatePrice(res));
        setTotal(calculateTotal(res));
      })
      .catch((err) => {
        console.log("Error:");
      });
  };

  const handleError = (err) => console.error(err);

  return (
    <ChakraProvider>
      <BarcodeReader onError={handleError} onScan={handleScan} />
      <Grid minH="100vh">
        <HStack w="full" spacing="0px" align="flex-start">
          <VStack h="full" w="full" spacing="0px" align="flex-start">
            <HStack w="full" h={14} spacing="0px">
              <Box h={16} w="full">
                <Navbar />
              </Box>
            </HStack>
            <HStack w="full" h="full" spacing="0px">
              <HStack h="full" w={550} spacing="0px" align="flex-start">
                <MainSideBar scanData={scanData} />
              </HStack>
              <Divider orientation="vertical" />
              <HStack h="full" w="full" spacing="0px">
                <SummaryBar
                  gst={gst}
                  pst={pst}
                  itemName={itemName}
                  price={price}
                  total={total}
                  reset={resetData}
                />
              </HStack>
            </HStack>
          </VStack>
        </HStack>
      </Grid>
    </ChakraProvider>
  );
}
