using CsvHelper;
using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using PetProject2.Properties;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace PetProject2.Models
{
    public class SeedData
    {
        public static void EnsurePopulated(IApplicationBuilder app)
        {
            ApplicationDbContext context = app.ApplicationServices
            .GetRequiredService<ApplicationDbContext>();
            context.Database.Migrate();
        }


            public static List<Pet> testSeed()
        {
            List<Pet> pets = new List<Pet>();
            var textReader = new StringReader(Resources.Pets);
            var csv = new CsvReader(textReader);
            csv.Configuration.HasHeaderRecord = false;

            csv.Read();

            while (csv.Read())
            {
                 var record = csv.GetRecord<Pet>();
                 pets.Add(record);
            }

            return pets;
        }
    }
}
