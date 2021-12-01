import React from "react";
import { ChakraProvider, Box } from "@chakra-ui/react";
import Navbar from "./Navbar/index";
import MainSideBar from "./MainSideBar";
import SummaryBar from "./SummaryBar";
import {
  Divider,
  Center,
  Grid,
  GridItem,
  Stack,
  HStack,
  VStack,
  StackDivider,
} from "@chakra-ui/react";

function App() {
  return (
    <ChakraProvider>
      <Grid minH="100vh">
        <HStack w="full" spacing="0px" align="flex-start">
          <VStack h="full" w="full" spacing="0px" align="flex-start">
            <HStack w="full" h={14} bg="red.300" spacing="0px">
              <Box h={16} w="full" bg="red.300">
                <Navbar />
              </Box>
            </HStack>
            <HStack w="full" h="full" bg="red.300" spacing="0px">
              <HStack h="full" w={550} spacing="0px" align="flex-start">
                <MainSideBar />
              </HStack>
              <Divider orientation="vertical" />
              <HStack h="full" w="full" spacing="0px">
                <SummaryBar />
              </HStack>
            </HStack>
          </VStack>
        </HStack>
      </Grid>
    </ChakraProvider>
  );
}

export default App;
