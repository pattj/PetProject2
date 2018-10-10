using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;

namespace PetProject2.Migrations
{
    public partial class Initial : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Pets",
                columns: table => new
                {
                    AnimalID = table.Column<int>(nullable: false)
                        .Annotation("SqlServer:ValueGenerationStrategy", SqlServerValueGenerationStrategy.IdentityColumn),
                    pet_name = table.Column<string>(nullable: true),
                    pet_photo = table.Column<string>(nullable: true),
                    pet_gender = table.Column<string>(nullable: false),
                    pet_description = table.Column<string>(nullable: true),
                    pet_lastupdated = table.Column<string>(nullable: true),
                    pet_type = table.Column<string>(nullable: true),
                    shelter_id = table.Column<string>(nullable: true),
                    pet_breed1 = table.Column<string>(nullable: true),
                    pet_breed2 = table.Column<string>(nullable: true),
                    pet_detail = table.Column<string>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Pets", x => x.AnimalID);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Pets");
        }
    }
}
