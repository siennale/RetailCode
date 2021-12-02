import {
  Box,
  Text,
  VStack,
  HStack,
  Grid,
  GridItem,
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";

export default function MainSideBar(props) {
  const data = props.scanData;
  const [totalPrice, settotalPrice] = useState(0);

  useEffect(() => {
    let total = 0;
    data.forEach((row) => {
      total += row.data[4] ? row.data[3] * 1.12 : row.data[3];
    });
    settotalPrice(total);
    return () => {
      settotalPrice(0);
    };
  }, [props]);

  console.log(data);
  return (
    <Box w="full">
      <Text fontSize="md" p={2}>
        Summary
      </Text>
      <Table size="sm">
        <Thead>
          <Tr>
            <Th>Items</Th>
            <Th>Qty</Th>
            <Th isNumeric>Price</Th>
          </Tr>
        </Thead>
        <Tbody>
          {data.map((rowValue) => (
            <Tr>
              <Td>{rowValue.data[2]}</Td>
              <Td isNumeric>1</Td>
              <Td isNumeric>
                {(rowValue.data[4]
                  ? rowValue.data[3] * 1.12
                  : rowValue.data[3]
                ).toFixed(2)}
              </Td>
            </Tr>
          ))}
        </Tbody>
        <Tfoot>
          <Tr>
            <Th>Total</Th>
            <Th isNumeric>{totalPrice.toFixed(2)}</Th>
          </Tr>
        </Tfoot>
      </Table>
    </Box>
  );
}
