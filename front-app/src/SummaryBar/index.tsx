import React, { useState, useEffect } from "react";
import {
  Center,
  Heading,
  Text,
  Box,
  Button,
  VStack,
  HStack,
} from "@chakra-ui/react";

export default function SummaryBar(props) {
  return (
    <VStack w="full" h="full">
      <HStack h="full">
        <Box>
          <Center verticalAlign="true">
            <Heading>Item</Heading>
          </Center>
          <Center verticalAlign="true">
            <Text fontSize="lg">{props.itemName}</Text>
          </Center>
          <Center verticalAlign="true">
            <Text fontSize="lg">$ {props.price}</Text>
          </Center>
          <Center verticalAlign="true">
            <Text fontSize="lg">
              Tax GST = ${props.gst} PST = ${props.pst}
            </Text>
          </Center>
          <Center verticalAlign="true">
            <Text fontSize="lg">Total $ {props.total}</Text>
          </Center>
        </Box>
      </HStack>
      <HStack>
        <Box>
          <Button
            colorScheme="teal"
            size="md"
            p={3}
            m={4}
            variant="outline"
            onClick={props.reset}
          >
            Done
          </Button>
          <Button
            colorScheme="teal"
            size="md"
            p={3}
            m={4}
            variant="outline"
            onClick={props.reset}
          >
            Reset
          </Button>
        </Box>
      </HStack>
    </VStack>
  );
}
