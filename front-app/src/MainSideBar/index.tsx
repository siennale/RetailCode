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

export default function MainSideBar() {
  return (
    <Box w="full">
      <Text fontSize="md" p={2}>
        Summary
      </Text>
      {/* <Grid templateColumns="repeat(4, 1fr)" gap={6} p={2}>
        <GridItem colSpan={2}>
          <Text as="i" fontSize="sm">
            Items
          </Text>
        </GridItem>
        <GridItem colSpan={1}>
          <Text fontSize="sm" as="i">
            Qty
          </Text>
        </GridItem>
        <GridItem colSpan={1}>
          <Text fontSize="sm" as="i">
            Price
          </Text>
        </GridItem>
      </Grid> */}
      <Table size="sm">
        <Thead>
          <Tr>
            <Th>Items</Th>
            <Th>Qty</Th>
            <Th isNumeric>Price</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr>
            <Td>inches inches inches inchedc</Td>
            <Td isNumeric>25.4</Td>
            <Td isNumeric>25.4</Td>
          </Tr>
          <Tr>
            <Td>inches inches inches inchedc</Td>
            <Td isNumeric>25.4</Td>
            <Td isNumeric>25.4</Td>
          </Tr>
          <Tr>
            <Td>inches inches inches inchedc</Td>
            <Td isNumeric>25.4</Td>
            <Td isNumeric>25.4</Td>
          </Tr>
        </Tbody>
        {/* <Tfoot>
          <Tr>
            <Th>Total</Th>
            <Th></Th>
            <Th isNumeric>multiply by</Th>
          </Tr>
        </Tfoot> */}
      </Table>
    </Box>
  );
}
