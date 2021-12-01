import React from "react";
import { Container, Center, Heading, Text, Box } from "@chakra-ui/react";

export default function SummaryBar() {
  return (
    <Container maxW="container.xl" alignContent="center">
      <Box>
        <Center verticalAlign="true">
          <Heading as="i">Item</Heading>
        </Center>
        <Center verticalAlign="true">
          <Text fontSize="lg">Pop</Text>
        </Center>
        <Center verticalAlign="true">
          <Text fontSize="lg">$56</Text>
        </Center>
        <Center verticalAlign="true">
          <Text fontSize="lg">Tax GST = $5 PST = $4</Text>
        </Center>
        <Center verticalAlign="true">
          <Text fontSize="lg">Total $59</Text>
        </Center>
      </Box>
    </Container>
  );
}
